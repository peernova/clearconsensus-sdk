/*
 * clearconsensus-sdk
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import org.openapitools.client.model.TitaniumBenchmarkMetadata;
import org.openapitools.client.model.TitaniumChartSource;
import org.openapitools.client.model.TitaniumOutlierMetadata;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * TitaniumChartsResponseData
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-05-15T16:46:20.742886Z[UTC]")
public class TitaniumChartsResponseData {
  public static final String SERIALIZED_NAME_BENCHMARK = "benchmark";
  @SerializedName(SERIALIZED_NAME_BENCHMARK)
  private List<TitaniumBenchmarkMetadata> benchmark = null;

  public static final String SERIALIZED_NAME_CHART_SOURCES = "chartSources";
  @SerializedName(SERIALIZED_NAME_CHART_SOURCES)
  private List<TitaniumChartSource> chartSources = null;

  public static final String SERIALIZED_NAME_OUTLIERS = "outliers";
  @SerializedName(SERIALIZED_NAME_OUTLIERS)
  private List<TitaniumOutlierMetadata> outliers = null;

  public static final String SERIALIZED_NAME_TENORS = "tenors";
  @SerializedName(SERIALIZED_NAME_TENORS)
  private List<String> tenors = null;

  public TitaniumChartsResponseData() { 
  }

  public TitaniumChartsResponseData benchmark(List<TitaniumBenchmarkMetadata> benchmark) {
    
    this.benchmark = benchmark;
    return this;
  }

  public TitaniumChartsResponseData addBenchmarkItem(TitaniumBenchmarkMetadata benchmarkItem) {
    if (this.benchmark == null) {
      this.benchmark = new ArrayList<>();
    }
    this.benchmark.add(benchmarkItem);
    return this;
  }

   /**
   * Get benchmark
   * @return benchmark
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<TitaniumBenchmarkMetadata> getBenchmark() {
    return benchmark;
  }


  public void setBenchmark(List<TitaniumBenchmarkMetadata> benchmark) {
    this.benchmark = benchmark;
  }


  public TitaniumChartsResponseData chartSources(List<TitaniumChartSource> chartSources) {
    
    this.chartSources = chartSources;
    return this;
  }

  public TitaniumChartsResponseData addChartSourcesItem(TitaniumChartSource chartSourcesItem) {
    if (this.chartSources == null) {
      this.chartSources = new ArrayList<>();
    }
    this.chartSources.add(chartSourcesItem);
    return this;
  }

   /**
   * Get chartSources
   * @return chartSources
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<TitaniumChartSource> getChartSources() {
    return chartSources;
  }


  public void setChartSources(List<TitaniumChartSource> chartSources) {
    this.chartSources = chartSources;
  }


  public TitaniumChartsResponseData outliers(List<TitaniumOutlierMetadata> outliers) {
    
    this.outliers = outliers;
    return this;
  }

  public TitaniumChartsResponseData addOutliersItem(TitaniumOutlierMetadata outliersItem) {
    if (this.outliers == null) {
      this.outliers = new ArrayList<>();
    }
    this.outliers.add(outliersItem);
    return this;
  }

   /**
   * Get outliers
   * @return outliers
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<TitaniumOutlierMetadata> getOutliers() {
    return outliers;
  }


  public void setOutliers(List<TitaniumOutlierMetadata> outliers) {
    this.outliers = outliers;
  }


  public TitaniumChartsResponseData tenors(List<String> tenors) {
    
    this.tenors = tenors;
    return this;
  }

  public TitaniumChartsResponseData addTenorsItem(String tenorsItem) {
    if (this.tenors == null) {
      this.tenors = new ArrayList<>();
    }
    this.tenors.add(tenorsItem);
    return this;
  }

   /**
   * Get tenors
   * @return tenors
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<String> getTenors() {
    return tenors;
  }


  public void setTenors(List<String> tenors) {
    this.tenors = tenors;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumChartsResponseData titaniumChartsResponseData = (TitaniumChartsResponseData) o;
    return Objects.equals(this.benchmark, titaniumChartsResponseData.benchmark) &&
        Objects.equals(this.chartSources, titaniumChartsResponseData.chartSources) &&
        Objects.equals(this.outliers, titaniumChartsResponseData.outliers) &&
        Objects.equals(this.tenors, titaniumChartsResponseData.tenors);
  }

  @Override
  public int hashCode() {
    return Objects.hash(benchmark, chartSources, outliers, tenors);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumChartsResponseData {\n");
    sb.append("    benchmark: ").append(toIndentedString(benchmark)).append("\n");
    sb.append("    chartSources: ").append(toIndentedString(chartSources)).append("\n");
    sb.append("    outliers: ").append(toIndentedString(outliers)).append("\n");
    sb.append("    tenors: ").append(toIndentedString(tenors)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("benchmark");
    openapiFields.add("chartSources");
    openapiFields.add("outliers");
    openapiFields.add("tenors");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumChartsResponseData
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumChartsResponseData.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumChartsResponseData is not found in the empty JSON string", TitaniumChartsResponseData.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumChartsResponseData.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumChartsResponseData` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      JsonArray jsonArraybenchmark = jsonObj.getAsJsonArray("benchmark");
      if (jsonArraybenchmark != null) {
        // ensure the json data is an array
        if (!jsonObj.get("benchmark").isJsonArray()) {
          throw new IllegalArgumentException(String.format("Expected the field `benchmark` to be an array in the JSON string but got `%s`", jsonObj.get("benchmark").toString()));
        }

        // validate the optional field `benchmark` (array)
        for (int i = 0; i < jsonArraybenchmark.size(); i++) {
          TitaniumBenchmarkMetadata.validateJsonObject(jsonArraybenchmark.get(i).getAsJsonObject());
        };
      }
      JsonArray jsonArraychartSources = jsonObj.getAsJsonArray("chartSources");
      if (jsonArraychartSources != null) {
        // ensure the json data is an array
        if (!jsonObj.get("chartSources").isJsonArray()) {
          throw new IllegalArgumentException(String.format("Expected the field `chartSources` to be an array in the JSON string but got `%s`", jsonObj.get("chartSources").toString()));
        }

        // validate the optional field `chartSources` (array)
        for (int i = 0; i < jsonArraychartSources.size(); i++) {
          TitaniumChartSource.validateJsonObject(jsonArraychartSources.get(i).getAsJsonObject());
        };
      }
      JsonArray jsonArrayoutliers = jsonObj.getAsJsonArray("outliers");
      if (jsonArrayoutliers != null) {
        // ensure the json data is an array
        if (!jsonObj.get("outliers").isJsonArray()) {
          throw new IllegalArgumentException(String.format("Expected the field `outliers` to be an array in the JSON string but got `%s`", jsonObj.get("outliers").toString()));
        }

        // validate the optional field `outliers` (array)
        for (int i = 0; i < jsonArrayoutliers.size(); i++) {
          TitaniumOutlierMetadata.validateJsonObject(jsonArrayoutliers.get(i).getAsJsonObject());
        };
      }
      // ensure the json data is an array
      if (jsonObj.get("tenors") != null && !jsonObj.get("tenors").isJsonArray()) {
        throw new IllegalArgumentException(String.format("Expected the field `tenors` to be an array in the JSON string but got `%s`", jsonObj.get("tenors").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumChartsResponseData.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumChartsResponseData' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumChartsResponseData> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumChartsResponseData.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumChartsResponseData>() {
           @Override
           public void write(JsonWriter out, TitaniumChartsResponseData value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumChartsResponseData read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumChartsResponseData given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumChartsResponseData
  * @throws IOException if the JSON string is invalid with respect to TitaniumChartsResponseData
  */
  public static TitaniumChartsResponseData fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumChartsResponseData.class);
  }

 /**
  * Convert an instance of TitaniumChartsResponseData to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

